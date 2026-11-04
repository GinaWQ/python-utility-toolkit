# Звіт до лабораторної роботи 02

**Тема:** Налаштування середовища розробки та Git workflow

## 1. Загальні відомості

- **ПІБ:** Полезнюк Аліна Вікторівна
- **Група:** ІПЗ21
- **Роль у команді:** Developer (розробка модуля калькулятора, оформлення документації)
- **GitHub-акаунт:** alina2010polezniuk-blip
- **Репозиторій:** https://github.com/GinaWQ/python-utility-toolkit
- **Проєкт:** Python Utility Toolkit — набір невеликих Python-утиліт (калькулятор, конвертер температур, конвертер одиниць, генератор паролів)

## 2. Особистий внесок

### Гілки

| Гілка | Призначення |
|-------|-------------|
| `feature/calculator` | модуль калькулятора (`calculator.py`) |
| `docs/project-documentation` | оновлення README.md та .gitignore |
| `docs/readme-clone-url` | виправлення команди клонування в README (тренування конфлікту) |
| `docs/add-changelog-and-report` | додавання CHANGELOG.md та звіту |

### Коміти

| Коміт | Опис |
|-------|------|
| [4bb5aa7](https://github.com/GinaWQ/python-utility-toolkit/commit/4bb5aa7) | `feat(calculator): add basic arithmetic operations` — модуль калькулятора: add, subtract, multiply, divide із перевіркою ділення на нуль (`ValueError`) |
| [5215ecf](https://github.com/GinaWQ/python-utility-toolkit/commit/5215ecf) | `docs: improve project documentation` — розширений README.md (опис, структура, встановлення, запуск) та форматування .gitignore |

### Pull Request-и

| PR | Опис |
|----|------|
| [#7](https://github.com/GinaWQ/python-utility-toolkit/pull/7) | `feature/calculator` → `main` |
| [#8](https://github.com/GinaWQ/python-utility-toolkit/pull/8) | `docs/project-documentation` → `main` |
| [#5](https://github.com/GinaWQ/python-utility-toolkit/pull/5) | `feature/unit-converter` → `main` (злиття PR колеги) |
| [ЗАПОВНИТИ: номер PR з конфліктом](https://github.com/GinaWQ/python-utility-toolkit/pulls) | вирішення конфлікту в README.md |
| [ЗАПОВНИТИ: номер PR зі звітом](https://github.com/GinaWQ/python-utility-toolkit/pulls) | додавання CHANGELOG.md та звіту |

## 3. Вирішений конфлікт злиття

**Ситуація.** Дві гілки від `main` змінили один і той самий рядок у `README.md` (рядок з командою `git clone`):

- `docs/readme-clone-url` — [ЗАПОВНИТИ: що саме змінила одна гілка];
- друга гілка — [ЗАПОВНИТИ: що саме змінила інша гілка].

Після злиття першого Pull Request GitHub показав у другому повідомлення про конфлікт: Git не зміг автоматично вирішити, чия версія рядка правильна.

**Як вирішено.**
1. Відкрила Pull Request із конфліктом та натиснула **Resolve conflicts**.
2. У файлі з'явилися маркери `<<<<<<<`, `=======`, `>>>>>>>`: між ними лежать дві версії одного рядка.
3. Залишила один правильний варіант рядка, а маркери видалила.
4. Натиснула **Mark as resolved**, потім **Commit merge**.
5. Злила Pull Request у `main`.

**Скріншот конфлікту:**

[ЗАПОВНИТИ: вставити скріншот сторінки з конфліктом / редактора з маркерами]

## 4. Рівень 3: Issues та реліз

- **Issues:**
  - [#1](https://github.com/GinaWQ/python-utility-toolkit/issues/1) — `feat: add password generator module`;
  - [ЗАПОВНИТИ: посилання на Issue про CHANGELOG і звіт].
- **Зв'язок Issue та Pull Request:** у описі PR використано `Closes #N`, тому Issue закривається автоматично після злиття.
- **Реліз:** [v1.0.0](https://github.com/GinaWQ/python-utility-toolkit/releases) — [ЗАПОВНИТИ: посилання на реліз після створення].
- **`.gitignore`:** містить `__pycache__/`, `*.pyc`, `.venv/`, `.env`, `.vscode/`.
- **VS Code:** [ЗАПОВНИТИ тільки якщо реально робила: що саме зробила через панель Source Control].

## 5. Висновки

У ході лабораторної роботи я попрацювала в командному репозиторії за схемою Feature Branch Workflow: створювала окремі гілки для функцій, робила коміти зі зрозумілими повідомленнями та зливала зміни через Pull Request. Я навчилася вирішувати конфлікти злиття, коли дві гілки змінюють один рядок, і розумію, чому для цього потрібно підтягувати актуальну `main`. Також ознайомилася з Issues, `.gitignore`, тегами та GitHub Release як із частиною професійного процесу розробки.
