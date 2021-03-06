import json
import pandas as pd
import matplotlib.pyplot as plt

search_results = []
for i in range(1, 10):
    with open(f'searchResults{i}.json', 'r') as myfile:
        data = myfile.read()
    results = json.loads(data)
    search_results.append(results['data'])

search_results = [item for subl in search_results for item in subl]

slim_search_results = [
    {
        'subject': course['subject'],
        'courseTitle': course['courseTitle'],
        'maximumEnrollment': course['maximumEnrollment'],
        'enrollment': course['enrollment'],
    }
    for course in search_results
]
df = pd.DataFrame(slim_search_results, columns=['subject', 'courseTitle', 'maximumEnrollment', 'enrollment'])
plt.hist(df['enrollment'], bins=50, log=True)
plt.title('Histogram of class enrollment at Rice on a log scale')
plt.show()

total_enrollment = 0
total_courses = len(slim_search_results)
total_enrollment_greater_50 = 0
total_course_greater_50 = 0
total_course_greater_1 = 0
courses_greater_50 = []
for course in slim_search_results:
    total_enrollment += course['enrollment']
    if course['enrollment'] > 1:
        total_course_greater_1 += 1
    if course['enrollment'] > 50:
        courses_greater_50.append(course['courseTitle'])
        total_enrollment_greater_50 += course['enrollment']
        total_course_greater_50 += 1

print(f'Total Courses: {total_courses}')
print(
    f'Percent of classes greater than 50 out of all classes, including those with 1 student enrolled: {total_course_greater_50 / total_courses}')
print(f'Percent of classes greater than 50: {total_course_greater_50 / total_course_greater_1}')
print(f'Percent of classes greater than 50 weighted for class size: {total_enrollment_greater_50 / total_enrollment}')
