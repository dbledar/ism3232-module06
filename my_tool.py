# my_tool.py
# Author: Darian Peters


class AssignmentTool:
    """A tool that searches a list of assignments for deadlines"""

    def __init__(self, assignments):
        self.assignments = assignments

    def find_assignment(self, text):
        """Return the first known instance of a given assignment."""
        for assignment in self.assignments:
            if assignment in text.upper():
                return assignment
        return None

    def find_deadline(self, assignment):
        """Return the deadline for a given assignment."""
        return self.assignments.get(assignment)
