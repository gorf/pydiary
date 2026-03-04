## Cursor Cloud specific instructions

### Project Overview

PyDiary is a legacy Python 2 / Django blog system. See `README` for the original project description.

### Runtime Requirements

- **Python 2.7.18** via pyenv (installed at `~/.pyenv/versions/2.7.18`)
- **Django 1.5.12** (installed via pip in pyenv Python 2.7)
- **Pillow 6.2.2** (PIL replacement for CAPTCHA)
- pyenv is initialized in `~/.bashrc`; new shells auto-activate Python 2.7.18

### Key Gotchas

- **Python 2 only**: The codebase uses Python 2 syntax (`except X,e:`, `print` statements, `xmlrpclib`, `cStringIO`, `__unicode__`). It will not run on Python 3.
- **Django version**: Django 1.5.12 is used. The code mixes conventions from Django 1.1 and 1.5 eras. Templates use quoted `{% url "name" %}` syntax (requires Django >= 1.5), but model `save()` methods only accept `(force_insert, force_update)` without the `using` parameter added in Django 1.2+. This means `QuerySet.create()` calls fail — existing tests in `tests/tests.py` are broken by this pre-existing incompatibility.
- **Database**: For local dev, `pydiary/settings.py` is configured to use SQLite3 (file: `db.sqlite3`). The original code targets PostgreSQL. The settings file is in `.gitignore` so local changes aren't tracked.
- **No lint tooling**: There is no linter configured (no flake8, pylint, etc.). Code style follows Python 2 / PEP 8 conventions.

### Running the Dev Server

```bash
cd /workspace
python manage.py runserver 0.0.0.0:8000
```

Admin: `http://localhost:8000/admin/` (credentials: admin / admin123)

### Running Tests

```bash
cd /workspace
python manage.py test tests
```

Note: Tests fail due to the pre-existing `save()` method compatibility issue described above. The web application itself functions correctly.

### Database Reset

To reset the database from scratch:
```bash
cd /workspace
rm -f db.sqlite3
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell
```
