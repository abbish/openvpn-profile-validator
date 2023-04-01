# parallel_task.py
import threading


def run_tasks_in_parallel(tasks, num_threads):
    def do_task(task):
        result = task()
        return result

    threads = []
    results = []

    def thread_handler():
        while True:
            try:
                task = tasks.pop(0)
            except IndexError:
                break

            result = do_task(task)
            results.append(result)

    for i in range(num_threads):
        thread = threading.Thread(target=thread_handler)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results
