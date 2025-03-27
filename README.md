# NameDropper 👤💥

The smartest, sassiest name extraction tool on the block.

**NameDropper** takes a full name in *any language* or script — Latin, Chinese, Arabic, Korean, you name it — and extracts the parts that matter: first name, given name, last name (eventually), and maybe a bit more.

Whether you're personalizing an email, building a profile, or just want to call someone the right thing — NameDropper's got your back.

---

## 🚀 Features

- 🌍 Multilingual & multicultural name detection
- ✂️ Language-specific name extraction
- 💡 Confidence scoring so you know when to trust it
- 🧠 Modular handler system — plug in new cultures easily
- 🐳 Docker-ready & FastAPI-powered
- 🧪 Tested with native-script names like `王偉`, `山田太郎`, `김민지`, `فاطمة الزهراء`, and more

---

## 📦 Example API Response

```json
{
  "first_name": "Wei",
  "from_model": false,
  "confidence": 0.8,
  "language": "zh"
}
```

---

## 🛠 Usage

```bash
docker run -p 8000:8000 namedropper
```

Then hit it with:

```bash
curl -X POST http://localhost:8000/extract_first_name \
  -H "Content-Type: application/json" \
  -d '{"full_name": "王偉"}'
```

---

## 🌱 Future Plans

- 🔍 Extract full name components: title, first, middle, last
- 🔗 Name normalization & formatting
- 🧾 Probabilistic parsing based on large corpora
- 🤝 Nickname resolution and alias mapping

---

## 🙌 Credits

This project was generated with 💡 and ✨ by **ChatGPT**, acting as architect, engineer, and pun generator.

**[The user]** is the good shepherd of this project — shaping the vision, asking all the right questions, and making sure this thing ships.

---

## 📄 License

MIT — drop names responsibly.
