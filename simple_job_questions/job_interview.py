import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def job_interview_test():
    engine.reset()      # Allows us to run tests multiple times.

    # STUDENTS: you will need to edit the name of your rule file here
    engine.activate('job_interview_rules')

    print("doing proof")

    try:
        # STUDENTS: you will need to edit this line
        with engine.prove_goal('job_interview_rules.links($links)') as gen:
            for vars, plan in gen:
                print("Here are some of the questions you should practice:")
                for index, item in enumerate(vars['links']):
                    # STUDENTS: you will need to edit this line
                    print(f"\n{index + 1}. {item}")

    except Exception:
        print("in exception")
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
