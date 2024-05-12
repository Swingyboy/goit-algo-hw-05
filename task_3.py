import argparse
import pandas as pd
from task_utils.perform_tests import run_tests
from task_utils.report_generator import generate_html_report, save_html_report, open_html_report_in_browser


def main(runs_number: int = 3):
    res = pd.DataFrame(columns=["Pattern Presence", "Algorithm",  "Time", "Text Length", "Pattern Length"])
    result = run_tests(res, runs_number=runs_number)
    html_content = generate_html_report(result,
                                        runs_number=runs_number
                                        )
    save_html_report(html_content)
    open_html_report_in_browser()


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--runs", type=int, default=3)

    main(runs_number=args.parse_args().runs)
