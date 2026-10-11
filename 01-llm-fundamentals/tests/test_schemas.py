
import pytest
from pydantic import ValidationError

from task_extractor.schemas import Task, TaskExtraction


def test_valid_task():
    task = Task(
        description="Prepare invoice",
        owner="Maya",
        deadline="Friday",
        priority="high",
    )

    assert task.owner == "Maya"
    assert task.priority == "high"


def test_unknown_owner():
    task = Task(description="Review contract")

    assert task.owner is None
    assert task.deadline is None


def test_invalid_priority():
    with pytest.raises(ValidationError):
        Task(
            description="Prepare invoice",
            priority="super urgent",
        )


def test_empty_description():
    with pytest.raises(ValidationError):
        Task(description="")


def test_extraction_contains_tasks():
    result = TaskExtraction(
        tasks=[
            Task(description="Prepare invoice"),
            Task(description="Review contract"),
        ]
    )

    assert len(result.tasks) == 2
