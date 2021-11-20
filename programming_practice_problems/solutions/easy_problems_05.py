import csv
import io
import unittest
from typing import Any, Dict, List
from unittest.mock import patch

# 5. The results from the mayor's race have been reported by each precinct as follows:
#
#           Candidate  Candidate  Candidate  Candidate
# Precinct      A          B          C          D
#    1         192        48         206        37
#    2         147        90         312        21
#    3         186        12         121        38
#    4         114        21         408        39
#    5         267        13         382        29
#
# Write a program to do the following:
#
# a. Read the raw vote totals from a data file that contains one row for each precinct.
#
# b. Display the table with appropriate headings for the rows and columns.
#
# c. Compute and display the total number of votes received by each candidate and
# the percent of the total votes cast.
#
# d. If any one candidate received over 50% of the votes, the program should print
# a message declaring that candidate the winner.
#
# e. If no candidate received 50% of the votes, the program should print a message
# declaring a run-off between the two candidates receiving the highest number of
# votes; the two candidates should be identified by their letter names.
#
# f. For testing, run the program with the above data, and also with another
# data file where Candidate C receives only 108 votes in precinct 4.


def print_table(rows: List[Dict[str, Any]]) -> None:
    buffer: List[str] = []
    cols: Dict[str, int] = {}

    for name in rows[0].keys():
        cols[name] = len(name)

    empty_line = ""
    separator_line = character_string("-", table_height(cols))
    header_line = "| " + " | ".join(cols.keys()) + " |"

    buffer.append(empty_line)
    buffer.append(separator_line)
    buffer.append(header_line)
    buffer.append(separator_line)

    for row in rows:
        row_line = "|"
        for key, value in row.items():
            rest_spaces = len(key) - len(str(value))
            cell = str(value) + character_string(" ", rest_spaces)
            row_line = row_line + " " + cell + " |"

        buffer.append(row_line)
        buffer.append(separator_line)

    for line in buffer:
        print(line)


def table_height(cols: Dict[str, int]) -> int:
    values_len = sum(cols.values())
    spaces_len = len(cols) * 2
    separators_len = len(cols) + 1

    return values_len + spaces_len + separators_len


def character_string(character: str, len: int) -> str:
    characters: List[str] = []

    for _ in range(len):
        characters.append(character)

    return "".join(characters)


def to_votes(csv_path: str) -> List[Dict]:
    votes: List[Dict] = []

    with open(csv_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            votes.append(row)

    return votes


def to_results(candidates: Dict[str, int]) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    cast = sum(candidates.values())

    for candidate, total_votes in candidates.items():
        letter: str = candidate.split(" ")[1]
        cast_percent: float = round((total_votes * 100 / cast), 2)

        candidate_results = {
            "Candidate": letter,
            "Total votes": total_votes,
            "Cast %": cast_percent,
        }

        results.append(candidate_results)

    return results


def to_candidates(votes: List[Dict]) -> Dict[str, int]:
    candidates: Dict[str, int] = {}

    for vote in votes:
        for key in vote.keys():
            if key != "Precinct":
                if key in candidates.keys():
                    candidates[key] = candidates[key] + int(vote[key])
                else:
                    candidates[key] = int(vote[key])

    return candidates


def check_results(results: List[Dict[str, Any]]) -> str:
    results.sort(key=lambda c: -c["Cast %"])

    if results[0]["Cast %"] > 50:
        return "The winner is Candidate {0}".format(results[0]["Candidate"])
    else:
        return "Run off between {0} and {1}".format(
            results[0]["Candidate"], results[1]["Candidate"]
        )


class Test(unittest.TestCase):
    def test_a_read_the_raw_vote_totals(self):
        csv_path_file = "solutions/easy_problems_05_data_winner.csv"
        votes = to_votes(csv_path_file)
        self.assertEqual(5, len(votes))

    def test_b_display_table(self):
        self.maxDiff = None
        expected_table = """
--------------------------------------------------------------------
| Precinct | Candidate A | Candidate B | Candidate C | Candidate D |
--------------------------------------------------------------------
| 1        | 192         | 48          | 206         | 37          |
--------------------------------------------------------------------
| 2        | 147         | 90          | 312         | 21          |
--------------------------------------------------------------------
| 3        | 186         | 12          | 121         | 38          |
--------------------------------------------------------------------
| 4        | 114         | 21          | 408         | 39          |
--------------------------------------------------------------------
| 5        | 267         | 13          | 382         | 29          |
--------------------------------------------------------------------
"""

        with patch(target="sys.stdout", new_callable=io.StringIO) as mocked_out:
            csv_path_file = "solutions/easy_problems_05_data_winner.csv"
            votes = to_votes(csv_path_file)
            print_table(votes)
            self.assertEqual(expected_table, mocked_out.getvalue())

    def test_c_display_total_number_of_votes_and_cast_percent(self):
        self.maxDiff = None
        expected_table = """
------------------------------------
| Candidate | Total votes | Cast % |
------------------------------------
| A         | 906         | 33.77  |
------------------------------------
| B         | 184         | 6.86   |
------------------------------------
| C         | 1429        | 53.26  |
------------------------------------
| D         | 164         | 6.11   |
------------------------------------
"""
        with patch(target="sys.stdout", new_callable=io.StringIO) as mocked_out:
            csv_path_file = "solutions/easy_problems_05_data_winner.csv"
            votes = to_votes(csv_path_file)
            candidates = to_candidates(votes)
            results = to_results(candidates)
            print_table(results)
            self.assertEqual(expected_table, mocked_out.getvalue())

    def test_d_display_winner(self):
        csv_path_file = "solutions/easy_problems_05_data_winner.csv"
        votes = to_votes(csv_path_file)
        candidates = to_candidates(votes)
        results = to_results(candidates)
        self.assertEqual("The winner is Candidate C", check_results(results))

    def test_d_display_run_off(self):
        csv_path_file = "solutions/easy_problems_05_data_run_off.csv"
        votes = to_votes(csv_path_file)
        candidates = to_candidates(votes)
        results = to_results(candidates)
        self.assertEqual("Run off between C and A", check_results(results))
