import statistics as st

marks = [78, 65, 72]
marks.sort()

mean_marks = st.mean(marks)
print(f"Mean Mark : {mean_marks}")
median_marks = st.median(marks)
print(f"Median Marks : {median_marks}")