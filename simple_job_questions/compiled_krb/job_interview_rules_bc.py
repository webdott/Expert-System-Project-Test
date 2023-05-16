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

def midlevel_software_links(rule, arg_patterns, arg_context):
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
              "job_interview_rules.midlevel_software_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.midlevel_software_links: got unexpected plan from when clause 3"
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

def midlevel_data_links(rule, arg_patterns, arg_context):
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
              "job_interview_rules.midlevel_data_links: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              with engine.prove('job_interview_questions', 'experience_level', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "job_interview_rules.midlevel_data_links: got unexpected plan from when clause 3"
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
                  (pattern.pattern_literal(("https://leetcode.com/problems/two-sum/", "https://leetcode.com/problems/single-number/", "https://leetcode.com/problems/move-zeroes/", "https://leetcode.com/problems/majority-element/", "https://leetcode.com/problems/reverse-bits/", "https://leetcode.com/problems/palindrome-number/", "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "https://leetcode.com/problems/generate-parentheses/", "https://leetcode.com/problems/search-in-rotated-sorted-array/", "https://leetcode.com/problems/group-anagrams/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('midlevel_software_links', This_rule_base, 'links',
                  midlevel_software_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/intersection-of-two-arrays-ii/", "https://leetcode.com/problems/missing-number/", "https://leetcode.com/problems/symmetric-tree/", "https://leetcode.com/problems/design-hashmap/", "https://leetcode.com/problems/reverse-words-in-a-string/", "https://leetcode.com/problems/number-of-islands/", "https://leetcode.com/problems/basic-calculator/", "https://leetcode.com/problems/implement-queue-using-stacks/", "https://leetcode.com/problems/regular-expression-matching/", "https://leetcode.com/problems/string-to-integer-atoi/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('senior_software_links', This_rule_base, 'links',
                  senior_software_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/", "https://leetcode.com/problems/top-k-frequent-elements/", "https://leetcode.com/problems/number-of-islands/", "https://leetcode.com/problems/sudoku-solver/", "https://leetcode.com/problems/wildcard-matching/", "https://leetcode.com/problems/max-points-on-a-line/", "https://leetcode.com/problems/the-skyline-problem/", "https://leetcode.com/problems/find-median-from-data-stream/", "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/", "https://leetcode.com/problems/lfu-cache/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('junior_data_links', This_rule_base, 'links',
                  junior_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/big-countries/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/employee-bonus/", "https://leetcode.com/problems/biggest-single-number/", "https://leetcode.com/problems/daily-leads-and-partners/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/find-followers-count/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/rearrange-products-table/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/calculate-special-bonus/?envType=study-plan-v2&id=top-sql-50",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('midlevel_data_links', This_rule_base, 'links',
                  midlevel_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/nth-highest-salary/", "https://leetcode.com/problems/consecutive-numbers/", "https://leetcode.com/problems/the-latest-login-in-2020/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/exchange-seats/", "https://leetcode.com/problems/market-analysis-i/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))
  
  bc_rule.bc_rule('senior_data_links', This_rule_base, 'links',
                  senior_data_links, None,
                  (pattern.pattern_literal(("https://leetcode.com/problems/department-top-three-salaries/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&id=top-sql-50", "https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&id=top-sql-50", "https://www.hackerrank.com/challenges/validating-postalcode/problem", "https://www.hackerrank.com/challenges/maximize-it/problem", "https://www.hackerrank.com/challenges/matrix-script/problem", "https://leetcode.com/problems/trips-and-users/", "https://leetcode.com/problems/human-traffic-of-stadium/", "https://leetcode.com/problems/capital-gainloss/", "https://leetcode.com/problems/movie-rating/",)),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('sans'),))


Krb_filename = '../job_interview_rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 17)),
    ((20, 25), (19, 19)),
    ((26, 26), (20, 20)),
    ((27, 32), (21, 21)),
    ((33, 33), (22, 22)),
    ((46, 50), (25, 38)),
    ((52, 57), (40, 40)),
    ((58, 58), (41, 41)),
    ((59, 64), (42, 42)),
    ((65, 65), (43, 43)),
    ((78, 82), (46, 59)),
    ((84, 89), (61, 61)),
    ((90, 90), (62, 62)),
    ((91, 96), (63, 63)),
    ((97, 97), (64, 64)),
    ((110, 114), (68, 81)),
    ((116, 121), (83, 83)),
    ((122, 122), (84, 84)),
    ((123, 128), (85, 85)),
    ((129, 129), (86, 86)),
    ((142, 146), (89, 102)),
    ((148, 153), (104, 104)),
    ((154, 154), (105, 105)),
    ((155, 160), (106, 106)),
    ((161, 161), (107, 107)),
    ((174, 178), (110, 123)),
    ((180, 185), (125, 125)),
    ((186, 186), (126, 126)),
    ((187, 192), (127, 127)),
    ((193, 193), (128, 128)),
)
