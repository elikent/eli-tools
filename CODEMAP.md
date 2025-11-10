# CODEMAP – eli-tools
_Quick function-level inventory_
_Updated: 2025-11-10_

---

## 🩺 Summary

| Category | Count | Notes |
|-----------|--------|-------|
| **Modules** | 3 | frame, fs, text_utils |
| **Functions complete** | 3 / 3 | 0 function pending |
---

src/eli_tools
 fs.py/                     # paths and files
  [x] get_one_path          # returns exactly one matching path from data_dir. raises an error if zero matching paths or more than one matching path

 text_utils.py/             # text utilITIES
  [x] remove_diacritics     # removes diacritics
  [x] canon                 # lower-cases all letters and replaces \s with hyphen

 log_utils.py/             # text utilITIES
  [x] report               # log results and optionally print


## 🚧 Next Steps

---

_This document serves as the 30-second mental map of the repo. Update it as functions are created or refactored._
