from crud import Trial, Trials


endpoints = [
    (Trial, "trial/<int:trial_id>"),
    (Trials, "trials")
]

__all__ = ['crud_api', 'endpoints']