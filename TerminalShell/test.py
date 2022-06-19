import multiprocessing
from multiprocessing import Process


def worker(x):
    name_proc = multiprocessing.current_process().name
    res = x*x
    print(name_proc, res)
    return res


def advance_worker(read, write):
    while not read.empty():
        name_proc = multiprocessing.current_process().name
        x = read.get()
        res = x*x
        print(name_proc, res)
        write.put(res)


"""

Каналы - Pipes.
Класс multiprocessing.Pipe() возвращает пару объектов, соединенных каналом, которые
по умолчанию являются duplex сторонним.

Два объекта соединения, возвращаемые multiprocessing.Pipe(), представляют два
конца канала. Каждый объект подключения имеет методы Pipe.send() - посылает данные
# в канал и Pipe.recv() - получает данные из канала.

"""


def pipe_worker(conn):
    conn.send([42, None, 'hello'])
    conn.close()


"""

Синхронизация между процессами на разных ядрах

"""


def sync_worker(lock, i):
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()


"""

Совместное использование состояния между процессами

-Использование общей памяти Shared memory.
данные могут быть сохранены на карте общей памяти с помощью multiprocessing.Value или
multiprocessing.Array. 

"""


def shared_worker(num, arr):
    num.value = 3.1415927
    for i in range(len(arr)):
        arr[i] = -arr[i]


"""

- Использование серверного процесса Server process.

Объект SyncManager, возвращаемый multiprocessing.Manager(), управляет серверным процессом,
который содержит объекты Python и  позволяет другим процессам манипулировать ими с помощью прокси-объектов.

"""


def proxy_worker(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == "__main__":

    # объект multiprocessing.Pool предлагает удобные средства параллельного выполнения
    # функции для нескольких входных значений, автоматически распределяя их по ядрам
    # процессора

    write = multiprocessing.Queue()
    read = multiprocessing.Queue()

    [read.put(x) for x in range(3, 7)]

    NUM_CORE = 6

    procs = []

    for i in range(NUM_CORE):
        p = Process(target=advance_worker, args=(read, write,))
        procs.append(p)
        p.start()

    [proc.join() for proc in procs]
    print(write.get() for _ in range(write.qsize()))

    parent_conn, child_conn = multiprocessing.Pipe()
    p = Process(target=pipe_worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

    lock = multiprocessing.Lock()

    for num in range(10):
        Process(target=sync_worker, args=(lock, num)).start()

    # d - числа с плавающей точкой с двойной точностью
    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))  # i - целое число

    # для большей гибкости можно использовать multiprocessing.ctypes, чтобы создавать кастомные
    # объекты ctypes, выделенные из памяти

    process = Process(target=shared_worker, args=(num, arr))
    process.start()
    process.join()

    print(num.value)
    print(arr[:])

    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=proxy_worker, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
