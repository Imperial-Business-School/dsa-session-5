test = {
  'name': 'test_ses04_solution_binary_search_count_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> binary_search_count([1, 3, 4, 5, 6, 6, 7], 5)
          (True, 1)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses04 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
