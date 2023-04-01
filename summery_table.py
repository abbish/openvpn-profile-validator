from colorama import Style
from prettytable import PrettyTable


def print_summary_table(results):
    results.sort(key=lambda x: x['accessibility'], reverse=True)

    num_total_files = len(results)
    num_accessible_files = sum(result['accessibility'] for result in results)
    num_inaccessible_files = num_total_files - num_accessible_files

    table = PrettyTable()
    table.title = f'OpenVPN Profile Accessibility Verification Results'
    table.field_names = ["Profile file", "Is accessible"]
    for result in results:
        table.add_row([result['file_name'], result['accessibility_output_str']])

    print(table)
    print(
        f'total: {Style.BRIGHT}{num_total_files}{Style.RESET_ALL} profiles, {Style.BRIGHT}{num_accessible_files}{Style.RESET_ALL} accessible, {Style.BRIGHT}{num_inaccessible_files}{Style.RESET_ALL} inaccessible')
