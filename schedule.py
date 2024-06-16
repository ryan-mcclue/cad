#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# edge-adjacency for when known up-front as oppose to having to calculate
def s(courses):
  e = {}
  for c in courses:
    course_num = c[0]
    prereqs_list = c[1]
    if course_num in e:
      e[course_num].append(prereqs_list)
    else:
      e[course_num] = [prereqs_list]

  num_courses = len(e) 

  for course_num in num_courses:
    if has_cycle(e, course_num, set(), {}):
      return False
  return True

def has_cycle(graph, course_num, seen):
  if course_num in seen:
    return True
  seen.add(course_num)
  for neighbours in graph[course_num]:
    if has_cycle()
  seen.remove(course_num)
