import os
from single_verifier import single_verify_profile
import threading


def do_task(task):
    result = task()
    return result


def batch_verify_profiles(profiles_dir, username, password, num_threads):
    tasks = []
    threads = []
    results = []
    files = sorted(os.listdir(profiles_dir))

    for file in files:
        if file.endswith('.ovpn'):
            file_path = os.path.join(profiles_dir, file)
            tasks.append(lambda profile_file=file_path: single_verify_profile(profile_file, username, password))

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
