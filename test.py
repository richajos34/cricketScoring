from game import simulate_ball

def test_simulate_ball():
    outcomes = [simulate_ball(None, None) for _ in range(1000)]
    assert 'wicket' in outcomes
    assert 'six' in outcomes
    print("Ball simulation test passed!")

test_simulate_ball()
