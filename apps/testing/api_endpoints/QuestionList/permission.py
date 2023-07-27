from rest_framework.permissions import BasePermission

from apps.testing.models import TestResult


class NotSolvedBefore(BasePermission):
    message = "You have already solved the test"

    def has_permission(self, request, view):
        # Get the user and category_name from the request and view
        user = request.user
        category_name = request.query_params.get("subject")
        if category_name is not None:
            # Check if the user has an existing TestResult record for the quiz
            return not TestResult.objects.filter(user=user, quiz__category__name=category_name).exists()

        return True
