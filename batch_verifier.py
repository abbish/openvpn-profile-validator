# batch_verifier.py
import os
from parallel_task import run_tasks_in_parallel

from single_verifier import single_verify_profile


def create_verify_task(file_path, username, password):
    return lambda: single_verify_profile(file_path, username, password)


def batch_verify_profiles(profiles_dir, username, password, num_threads):
    tasks = []
    files = sorted(os.listdir(profiles_dir))

    for file in files:
        if file.endswith('.ovpn'):
            file_path = os.path.join(profiles_dir, file)
            task = create_verify_task(file_path, username, password)
            tasks.append(task)

    results = run_tasks_in_parallel(tasks, num_threads)

    return results
