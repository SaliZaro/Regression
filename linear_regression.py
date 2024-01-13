import pandas as pd

df = pd.read_csv("data.csv")

def partial_loss_func(m_now, c_now, df, LearnRate):
    a = m_now
    b = c_now
    for i in df.index:
        m_now += ((a * df.loc[i, "SAT"] - df.loc[i, "GPA"]) * df.loc[i, "SAT"])
        c_now += (a * df.loc[i, "SAT"] - df.loc[i, "GPA"])
    return [m_now, c_now]

slope_initial = 0
y_intercept_initial = 0
LearnRate = 0.00001
no_of_iterations = 300

for i in range(0, no_of_iterations):
    if i % 50 == 0:
        print(f"completed no of iterations: {i}")

    # Use the original value of y_intercept_initial
    slope_initial = partial_loss_func(slope_initial, y_intercept_initial, df, LearnRate)[0]
    y_intercept_initial = partial_loss_func(slope_initial, y_intercept_initial, df, LearnRate)[1]

slope_final = slope_initial
y_intercept_final = y_intercept_initial

print(slope_final, y_intercept_final)