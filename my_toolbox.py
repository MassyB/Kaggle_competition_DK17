import pandas as pd

def save_submission(file_name, y_test):
    submission_df = pd.DataFrame({"Id": range(1, len(y_test) + 1),
                                  "prediction": y_test})
    submission_df.to_csv(file_name)
