"""Standalone tests — run without Django installed."""
import os


def test_version_defined():
    from clinic import __version__
    assert __version__ == "1.0.0"


def test_readme_exists():
    assert os.path.exists("README.md")


def test_changelog_exists():
    assert os.path.exists("CHANGELOG.md")


def test_architecture_doc_exists():
    assert os.path.exists("ARCHITECTURE.md")


def test_api_doc_exists():
    assert os.path.exists("API.md")


def test_dockerfile_exists():
    assert os.path.exists("Dockerfile")


def test_requirements_exists():
    assert os.path.exists("requirements.txt")


def test_requirements_has_django():
    with open("requirements.txt") as f:
        content = f.read().lower()
    assert "django" in content


def test_adr_exists():
    assert os.path.exists("docs/adr/0001-use-django-python.md")


def test_gitignore_exists():
    assert os.path.exists(".gitignore")


def test_ci_workflow_exists():
    assert os.path.exists(".github/workflows/ci.yml")
