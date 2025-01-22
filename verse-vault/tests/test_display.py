from utils.display import ornament


def test_ornament_output():
    output = ornament()
    assert output is not None, "Ornament function returned None"
    assert "_/_/_/_/_/" in output, "Expected ornamentation missing"
