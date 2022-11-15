# Script
`main.py`
```python
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
```

# Execution
```
$ docker build -t patinocode/patinocode:local . && docker run patinocode/patinocode:local
[+] Building 0.4s (8/8) FINISHED                                                                                                                                            
 => [internal] load build definition from Dockerfile                                                                                                                   0.0s
 => => transferring dockerfile: 114B                                                                                                                                   0.0s
 => [internal] load .dockerignore                                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.10-alpine                                                                                                  0.3s
 => [internal] load build context                                                                                                                                      0.0s
 => => transferring context: 2.01kB                                                                                                                                    0.0s
 => [1/3] FROM docker.io/library/python:3.10-alpine@sha256:447f4081c041840a1d4f66553d920f7878d260433b55497250546346546102fa                                            0.0s
 => CACHED [2/3] WORKDIR /app                                                                                                                                          0.0s
 => CACHED [3/3] COPY . .                                                                                                                                              0.0s
 => exporting to image                                                                                                                                                 0.0s
 => => exporting layers                                                                                                                                                0.0s
 => => writing image sha256:69bf0b89c916688433f1db09a7aebcd50056d427346eb5416147ac14ecb88b5e                                                                           0.0s
 => => naming to docker.io/patinocode/patinocode:local                                                                                                                 0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
✅
✅
{'skills': ['🐧', '🐙🐱', '☁️', '☸️'], 'languages': ['🐍', '☕📜', '🏗️']}
```