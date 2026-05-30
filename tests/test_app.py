"""Standalone tests — run with python -m pytest or python -m unittest."""
import os
import sys
import unittest
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent


class TestProjectStructure(unittest.TestCase):

    def test_readme_exists(self):
        self.assertTrue((BASE_DIR / "README.md").exists())

    def test_changelog_exists(self):
        self.assertTrue((BASE_DIR / "CHANGELOG.md").exists())

    def test_architecture_doc_exists(self):
        self.assertTrue((BASE_DIR / "ARCHITECTURE.md").exists())

    def test_api_doc_exists(self):
        self.assertTrue((BASE_DIR / "API.md").exists())

    def test_dockerfile_exists(self):
        self.assertTrue((BASE_DIR / "Dockerfile").exists())

    def test_requirements_exists(self):
        self.assertTrue((BASE_DIR / "requirements.txt").exists())

    def test_requirements_has_django(self):
        content = (BASE_DIR / "requirements.txt").read_text().lower()
        self.assertIn("django", content)

    def test_adr_exists(self):
        self.assertTrue((BASE_DIR / "docs" / "adr" / "0001-use-django-python.md").exists())

    def test_gitignore_exists(self):
        self.assertTrue((BASE_DIR / ".gitignore").exists())

    def test_ci_workflow_exists(self):
        self.assertTrue((BASE_DIR / ".github" / "workflows" / "ci.yml").exists())

    def test_version_in_setup(self):
        content = (BASE_DIR / "setup.cfg").read_text()
        self.assertIn("1.0.0", content)


if __name__ == "__main__":
    unittest.main()
