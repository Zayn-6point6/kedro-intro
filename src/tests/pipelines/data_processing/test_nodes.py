# import pandas as pd
# import pytest
# from kedro_tutorial.pipelines.data_processing.nodes import _parse_money
#
#
# def test_parse_money():
#     x_array = ["$100", "200,000", "$123,00", "100"]
#     import pdb;pdb.set_trace()
#     x = pd.Series(x_array)
#     x = _parse_money(x)
#
#     expected_array = [200.0, 200000.0, 12300.0, 100.0]
#     expected = pd.Series(expected_array)
#     assert x.all() == expected.all()
