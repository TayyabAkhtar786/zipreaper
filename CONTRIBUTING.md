# Contributing to ZipReaper

First off, thank you for your interest in contributing to ZipReaper! This document provides guidelines and instructions for contributing to the project.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)
- [Questions?](#questions)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. We pledge that:

- ✅ We value and respect all contributors
- ✅ We maintain a harassment-free environment
- ✅ We address issues promptly and fairly
- ✅ We foster knowledge sharing and growth

### Expected Behavior

- Be respectful and inclusive in all interactions
- Welcome diverse perspectives and ideas
- Provide constructive feedback
- Focus on the code, not the person
- Follow security and ethical guidelines

### Unacceptable Behavior

- Harassment, discrimination, or abuse
- Sharing of private information without consent
- Spam or low-quality contributions
- Attempts to bypass security controls
- Violation of laws or organizational policies

### Reporting Issues

If you witness or experience unacceptable behavior:
- Contact: [conduct@yourdomain.com]
- All reports will be handled confidentially
- No retaliation for good-faith reports

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- GitHub account
- Familiarity with command line
- Understanding of ZIP file formats & password attacks

### Environment Setup

```bash
# 1. Fork the repository
# Click "Fork" on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/zipreaper.git
cd zipreaper

# 3. Add upstream remote
git remote add upstream https://github.com/original_owner/zipreaper.git

# 4. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For testing tools

# 6. Verify installation
python3 zip_reaper.py
```

### Keeping Your Fork Updated

```bash
# Fetch updates from upstream
git fetch upstream

# Rebase your branch
git rebase upstream/main

# Push to your fork
git push origin main
```

---

## 🎯 Types of Contributions

### 1. Bug Fixes 🐛
**For**: Issues in existing functionality

```
Example: "Fix: Dictionary attack fails on certain ZIP formats"
Expected: Reproduce, fix, test, document
Impact: Critical/High/Medium/Low
```

**How to Contribute:**
1. Check [Issues](https://github.com/yourusername/zipreaper/issues) for existing reports
2. If not reported, create an issue with details
3. Create a branch: `git checkout -b fix/bug-description`
4. Fix the bug with tests
5. Submit pull request with reference to issue

### 2. Performance Improvements ⚡
**For**: Optimizing attack speed, memory usage, code efficiency

```
Example: "Feat: Implement multi-threading for 2x speed improvement"
Expected: Benchmark before/after, minimal code changes
Impact: Significant performance gain
```

**How to Contribute:**
1. Run baseline benchmarks: `python3 zip_reaper.py --benchmark`
2. Implement optimization
3. Run benchmarks again to prove improvement
4. Submit PR with performance metrics
5. Document the optimization technique

### 3. Feature Additions ✨
**For**: New capabilities that expand the tool's functionality

```
Example: "Feat: Add GPU acceleration support using CUDA"
Expected: Significant added value, backward compatible
Discussion: May require design review before implementation
```

**How to Contribute:**
1. Create an issue describing the feature
2. Discuss with maintainers (design review)
3. Get approval before starting implementation
4. Create feature branch: `git checkout -b feat/feature-name`
5. Implement with comprehensive tests
6. Submit PR with documentation

### 4. Documentation 📚
**For**: Improving guides, examples, explanations

```
Example: "Docs: Add Docker deployment guide"
Expected: Clear, actionable, well-formatted
Impact: Easier adoption by new users
```

**How to Contribute:**
1. Identify missing or unclear documentation
2. Create documentation branch: `git checkout -b docs/doc-name`
3. Write clear, concise documentation
4. Include examples where applicable
5. Submit PR for review

### 5. Research & Analysis 🔬
**For**: Password patterns, attack effectiveness, security insights

```
Example: "Research: Analysis of RockYou wordlist effectiveness against 2025 passwords"
Expected: Data-driven findings, statistical rigor
Publication: RESEARCH.md or new analysis document
```

**How to Contribute:**
1. Conduct research on security topic
2. Document findings with data
3. Analyze implications for ZipReaper
4. Submit as research paper or analysis document
5. Contribute to knowledge base

### 6. Security Improvements 🔒
**For**: Hardening, vulnerability fixes, defensive enhancements

```
Example: "Security: Add rate limiting for brute force protection"
Expected: Significant security benefit, no breaking changes
Disclosure: May require responsible disclosure process
```

**How to Contribute:**
1. Identify security improvement area
2. Research best practices & standards
3. Implement enhancement
4. Test thoroughly
5. Submit PR (or use private security process)

### 7. Testing & Quality 🧪
**For**: Test coverage, edge cases, quality assurance

```
Example: "Test: Add unit tests for wordlist validation"
Expected: Comprehensive coverage, no false positives
Impact: Higher code quality, faster development
```

**How to Contribute:**
1. Identify untested code paths
2. Create test branch: `git checkout -b test/test-description`
3. Write comprehensive tests
4. Verify test coverage
5. Submit PR with test results

---

## 🔄 Development Workflow

### Branch Naming Convention

```
TYPE/description-in-kebab-case

Types:
├─ fix/          → Bug fixes
├─ feat/         → Features
├─ docs/         → Documentation
├─ test/         → Tests
├─ perf/         → Performance
├─ refactor/     → Code refactoring
├─ chore/        → Maintenance tasks
└─ security/     → Security improvements
```

### Example Workflow

```bash
# 1. Create branch from main
git checkout -b feat/gpu-acceleration

# 2. Make changes
# Edit files...

# 3. Commit with clear messages
git add .
git commit -m "feat: Add CUDA GPU support for 5x speed improvement"

# 4. Push to fork
git push origin feat/gpu-acceleration

# 5. Create Pull Request on GitHub
# (GitHub will show "Create PR" button)

# 6. Address review feedback
# Make changes...
git add .
git commit -m "Address review: Add comprehensive GPU memory checks"
git push origin feat/gpu-acceleration

# 7. Merge after approval
# (Maintainer will merge to main)
```

---

## 📝 Coding Standards

### Python Style Guide: PEP 8

```python
# ✅ Good
def dictionary_attack(zip_file, wordlist):
    """
    Execute dictionary attack on ZIP file.
    
    Args:
        zip_file (str): Path to target ZIP file
        wordlist (str): Path to password wordlist
        
    Returns:
        str: Password if found, None otherwise
    """
    # Validate inputs
    if not os.path.exists(zip_file):
        raise FileNotFoundError(f"ZIP file '{zip_file}' not found")
    
    # Main logic
    result = None
    for password in passwords:
        if attempt_extraction(zip_file, password):
            result = password
            break
    
    return result


# ❌ Avoid
def attack(z, w):
    if not os.path.exists(z): raise FileNotFoundError()
    r=None;
    for p in w: 
        if extract(z,p): r=p; break
    return r
```

### Code Organization

```python
# ============================================================
#   SECTION HEADER (for major sections)
# ============================================================

# Comments above code, not inline
# Use meaningful variable names

CONSTANT_VALUES = "UPPERCASE_WITH_UNDERSCORES"

class ClassName:
    """Class docstring."""
    
    def method(self, param):
        """Method docstring."""
        pass
```

### Error Handling

```python
# ✅ Good
try:
    result = attempt_extraction(zip_file, password)
except zipfile.BadZipFile:
    print(RED + "Invalid ZIP file!")
    return None
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return None

# ❌ Avoid
try:
    result = attempt_extraction(zip_file, password)
except:  # Never bare except
    pass  # Silent failures are dangerous
```

### Comments & Documentation

```python
# ✅ Good
# Validate ZIP file before attempting extraction
if not zipfile.is_zipfile(zip_file):
    raise BadZipFileError("Invalid ZIP format")

# ❌ Avoid
# Loop through passwords  (obvious from code)
for p in passwords:
    attempt(p)
```

### Security in Code

```python
# ✅ Good
# Never log sensitive data
logger.info(f"Testing with wordlist: {wordlist}")  # OK
# logger.info(f"Password found: {password}")      # NEVER do this

# Validate all inputs
if not isinstance(attempts, int) or attempts < 0:
    raise ValueError("attempts must be non-negative integer")

# ❌ Avoid
# Hardcoded credentials
API_KEY = "sk-1234567890abcdef"  # NEVER do this

# Unvalidated input
os.system(f"unzip {user_input}")  # Vulnerable to injection
```

---

## 💬 Commit Guidelines

### Commit Message Format

```
TYPE: Brief description (50 chars max)

Longer description explaining the what and why (wrap at 72 chars).
Reference issue #123 if applicable.

Fixes #456
Relates to #789
```

### Types
- `feat:` New feature
- `fix:` Bug fix
- `perf:` Performance improvement
- `docs:` Documentation
- `test:` Test addition/modification
- `refactor:` Code restructuring
- `chore:` Maintenance
- `security:` Security hardening

### Examples

```bash
# Good
git commit -m "feat: Add GPU acceleration for 5x performance

Implement CUDA-based parallel password testing. Maintains backward
compatibility with CPU fallback. Requires NVIDIA drivers.

Relates to #42"

# Acceptable
git commit -m "fix: Resolve WordList encoding issue with Unicode passwords"

# ❌ Bad
git commit -m "fixed stuff"
git commit -m "wip: work in progress"
git commit -m "asdf"
```

### Commit Size

- ✅ **Atomic commits**: Each commit represents one logical change
- ❌ **Avoid**: Mixing unrelated changes in one commit
- ❌ **Avoid**: Massive commits touching 10+ files

---

## 🔀 Pull Request Process

### Before Opening a PR

1. **Sync with upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test thoroughly**
   ```bash
   python3 zip_reaper.py
   python3 -m pytest test/
   python3 -m pylint zip_reaper.py
   ```

3. **Check for conflicts**
   ```bash
   git log origin/main..HEAD  # Should show your commits only
   ```

4. **Update documentation**
   - Modify README.md if adding features
   - Update CHANGELOG.md with changes
   - Add docstrings to new functions

### PR Title Format

```
TYPE: Description (same as commit message)

Examples:
- feat: Add GPU acceleration support
- fix: Resolve Unicode password handling
- docs: Add Docker deployment guide
```

### PR Description Template

```markdown
## Description
Brief explanation of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing performed:
- Tested with weak.zip: ✓
- Tested with strong.zip: ✓
- Performance benchmarked: ✓

## Checklist
- [ ] Code follows style guide
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Commits are atomic
- [ ] Security review completed

## Related Issues
Fixes #123
Relates to #456
```

### PR Review Process

1. **Automated Checks**
   - ✅ Tests must pass
   - ✅ No merge conflicts
   - ✅ Code quality gates pass

2. **Manual Review**
   - Security review for sensitive changes
   - Code quality assessment
   - Documentation verification
   - Testing completeness

3. **Addressing Feedback**
   - Make requested changes
   - Commit with "Address review: ..." message
   - Do NOT force-push unless asked
   - Respond to all comments

4. **Approval & Merge**
   - Requires 2+ approvals for major changes
   - Maintainer performs squash merge
   - PR is closed

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python3 -m pytest

# Run specific test file
python3 -m pytest test/test_zip_handling.py

# Run with coverage
python3 -m pytest --cov=. --cov-report=html

# Run with verbose output
python3 -m pytest -v
```

### Writing Tests

```python
# test/test_zip_handling.py
import unittest
from zip_reaper import dictionary_attack

class TestZipHandling(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.weak_zip = "test_cases/weak.zip"
        self.wordlist = "test_data/small_wordlist.txt"
    
    def test_weak_password_found(self):
        """Test that weak passwords are successfully cracked."""
        result = dictionary_attack(self.weak_zip, self.wordlist)
        self.assertEqual(result, "password123")
    
    def test_invalid_zip_file(self):
        """Test handling of invalid ZIP files."""
        with self.assertRaises(FileNotFoundError):
            dictionary_attack("nonexistent.zip", self.wordlist)
    
    def test_wordlist_not_found(self):
        """Test handling when wordlist is missing."""
        with self.assertRaises(FileNotFoundError):
            dictionary_attack(self.weak_zip, "nonexistent.txt")
```

### Test Coverage Goals
- Minimum 80% code coverage
- All error paths tested
- Edge cases covered
- Performance benchmarked

---

## 📚 Documentation

### README.md Guidelines
- Keep it concise but comprehensive
- Include quick start section
- Add usage examples
- Reference other docs

### Code Documentation
- Docstrings on all functions/classes
- Comments for complex logic
- Type hints for clarity
- Examples in docstrings

### Format: Google Style

```python
def dictionary_attack(zip_file, wordlist, timeout=None):
    """
    Perform dictionary attack on password-protected ZIP file.
    
    This function iterates through a wordlist and attempts to extract
    the ZIP file with each password. It returns the first successful
    password or None if attack is exhausted.
    
    Args:
        zip_file (str): Path to the target ZIP file.
        wordlist (str): Path to password wordlist (one per line).
        timeout (int, optional): Attack timeout in seconds. Defaults to None.
    
    Returns:
        str: The cracked password if successful, None otherwise.
    
    Raises:
        FileNotFoundError: If zip_file or wordlist doesn't exist.
        BadZipFileError: If zip_file is not a valid ZIP file.
    
    Example:
        >>> password = dictionary_attack("archive.zip", "rockyou.txt")
        >>> if password:
        ...     print(f"Password found: {password}")
        ... else:
        ...     print("Attack unsuccessful")
    """
    pass
```

---

## ❓ Questions?

- **Usage Questions**: Check [README.md](./README.md) and [SECURITY.md](./SECURITY.md)
- **Contribution Questions**: Email [contributor@yourdomain.com]
- **Security Issues**: See [SECURITY.md#reporting-issues](./SECURITY.md#reporting-issues)
- **General Discussion**: Open a GitHub Discussion

---

## 🎉 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes for their version
- GitHub contributors graph
- Optional: Twitter/LinkedIn mention

---

## 📜 License

By contributing to ZipReaper, you agree that your contributions will be licensed under its MIT License.

---

<div align="center">

**Thank you for contributing to ZipReaper!**

Together we build better security tools.

[⬆ Back to Top](#contributing-to-zipreaper)

</div>
