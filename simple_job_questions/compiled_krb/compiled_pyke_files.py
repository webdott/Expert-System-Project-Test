# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'job_interview_rules.krb'):
           [1684257290.8058162, 'job_interview_rules_bc.py'],
         ('', '', 'job_interview_questions.kqb'):
           [1684257290.81004, 'job_interview_questions.qbc'],
        },
        compiler_version)

