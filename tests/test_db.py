from server.database import get_trial_data


def test_get_trial_data():
	user_id = 'test'
	trial_id = 0
	result = get_trial_data(user_id, trial_id)
	print result
	assert False
