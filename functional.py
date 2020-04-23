import os


def get_status(issues):
    status_list = []
    for issue in issues:
        if issue.fields.status.name not in status_list:
            status_list.append(issue.fields.status.name)
    return status_list


def sort_status_to_file(issues, listing):
    n = len(listing)
    massive = [[] for j in range(n)]
    for issue in issues:
        i = 0
        while i < n:
            if issue.fields.status.name == listing[i]:
                massive[i].append(issue.key + ' ' + issue.fields.summary)
            i += 1
    directory = os.getenv('HOMEPATH') + r"\Desktop\\file.txt"
    f = open(directory, 'tw')
    for i in range(0, n):
        f.write(str(listing[i]) + str(massive[i]) + '\n')
        i += 1
    f.close()


def sort_status(issues, listing):
    n = len(listing)
    massive = [[] for j in range(n)]
    for issue in issues:
        i = 0
        while i < n:
            if issue.fields.status.name == listing[i]:
                string = str(issue.key + ' ' + issue.fields.summary)
                massive[i].append(string)
            i += 1
    output = ""
    for i in range(0, n):
        output += (str(listing[i]) + '\n\n' + str(massive[i]) + '\n\n')
        i += 1
    return output
