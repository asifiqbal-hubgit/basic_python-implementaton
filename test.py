import pandas as pd
def test_dataframe_creation():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    assert df.shape == (3, 2)
    assert list(df.columns) == ['A', 'B']
    assert df['A'].tolist() == [1, 2, 3]
    assert df['B'].tolist() == [4, 5, 6]    
def test_series_creation():
    data = [10, 20, 30, 40]
    series = pd.Series(data)
    assert series.shape == (4,)
    assert series.tolist() == [10, 20, 30, 40]
    assert series.dtype == 'int64'
def test_series_indexing():
    
    data = [100, 200, 300]
    series = pd.Series(data, index=['a', 'b', 'c'])
    assert series['a'] == 100
    assert series['b'] == 200
    assert series['c'] == 300   
def test_dataframe_operations():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pd.DataFrame(data)
    df['Z'] = df['X'] + df['Y']
    assert 'Z' in df.columns
    assert df['Z'].tolist() == [5, 7, 9]
def test_series_operations():
    data = [1, 2, 3, 4]
    series = pd.Series(data)
    series_squared = series ** 2
    assert series_squared.tolist() == [1, 4, 9, 16]
print("All tests passed!")
test_dataframe_creation()