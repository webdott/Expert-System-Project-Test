# job_interview_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def junior_software_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.junior_software_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.junior_software_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (1,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def medium_software_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.medium_software_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.medium_software_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (2,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def senior_software_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.senior_software_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.senior_software_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (3,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def junior_data_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.junior_data_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.junior_data_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (1,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def medium_data_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.medium_data_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.medium_data_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (2,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def senior_data_links(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('job_interview_questions', 'role_application', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "job_interview_rules.senior_data_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.senior_data_links: got unexpected plan from when clause 3"
                  if context.lookup_data('sans') in (3,):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('job_interview_rules')
  
  bc_rule.bc_rule('junior_software_links', This_rule_base, 'links',
                  junior_software_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/two-sum/", "https://leetcode.com/problems/single-number/", "https://leetcode.com/problems/move-zeroes/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('medium_software_links', This_rule_base, 'links',
                  medium_software_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/intersection-of-two-arrays-ii/", "https://leetcode.com/problems/missing-number/", "https://leetcode.com/problems/symmetric-tree/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('senior_software_links', This_rule_base, 'links',
                  senior_software_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/", "https://leetcode.com/problems/top-k-frequent-elements/", "https://leetcode.com/problems/number-of-islands/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('junior_data_links', This_rule_base, 'links',
                  junior_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/big-countries/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&id=top-sql-50",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('medium_data_links', This_rule_base, 'links',
                  medium_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&id=top-sql-50",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('senior_data_links', This_rule_base, 'links',
                  senior_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/department-top-three-salaries/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&id=top-sql-50",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))


Krb_filename = '../job_interview_rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 6)),
    ((20, 25), (8, 8)),
    ((26, 26), (9, 9)),
    ((27, 32), (10, 10)),
    ((33, 33), (11, 11)),
    ((46, 50), (14, 16)),
    ((52, 57), (18, 18)),
    ((58, 58), (19, 19)),
    ((59, 64), (20, 20)),
    ((65, 65), (21, 21)),
    ((78, 82), (24, 26)),
    ((84, 89), (28, 28)),
    ((90, 90), (29, 29)),
    ((91, 96), (30, 30)),
    ((97, 97), (31, 31)),
    ((110, 114), (35, 39)),
    ((116, 121), (41, 41)),
    ((122, 122), (42, 42)),
    ((123, 128), (43, 43)),
    ((129, 129), (44, 44)),
    ((142, 146), (47, 49)),
    ((148, 153), (51, 51)),
    ((154, 154), (52, 52)),
    ((155, 160), (53, 53)),
    ((161, 161), (54, 54)),
    ((174, 178), (57, 59)),
    ((180, 185), (61, 61)),
    ((186, 186), (62, 62)),
    ((187, 192), (63, 63)),
    ((193, 193), (64, 64)),
)
