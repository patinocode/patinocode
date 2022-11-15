#!/usr/local/bin/python
# Python 3.10+

class DevOps:
  def __init__(
    self,
    python,
    javascript,
    terraform,
    linux,
    git,
    cloud,
    k8s
  ):
    self.python = python
    self.javascript = javascript
    self.terraform = terraform
    self.linux = linux
    self.git = git
    self.cloud = cloud
    self.k8s = k8s

    self.languages = []
    self.skills = []

  def validate(self):
    validate_langs = [
        True if language == "✅" else False for language in [self.python, self.javascript, self.terraform]
    ]

    if not False in validate_langs and print("✅") : return False

    validate_skills = [
        True if skill == "✅" else False for skill in [self.linux, self.git, self.cloud, self.k8s]
    ]

    if not False in validate_skills and print("✅") : return False

    return True

  def animate(self):
    if self.python == "✅":
        self.languages.append("🐍")
    if self.javascript:
        self.languages.append("☕📜")
    if self.terraform:
        self.languages.append("🏗️")
    if self.linux:
        self.skills.append("🐧")
    if self.git:
        self.skills.append("🐙🐱")
    if self.cloud:
        self.skills.append("☁️")
    if self.k8s:
        self.skills.append("☸️")

    print({"skills": self.skills, "languages": self.languages})

patino = DevOps( "✅", "✅", "✅", "✅", "✅", "✅", "✅" )
patino.validate()
patino.animate()
