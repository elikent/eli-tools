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
 file_transforms.py
  [x] combine_pdfs        # combine multiple pdfs into one
  [x] remove_pages        # remove pages from pdf
  [ ] convert_jpg_to_pdf  # convert jpg to pdf

 fs.py/                     # paths and file systems
  [x] get_one_path          # returns exactly one matching path from data_dir. raises an error if zero matching paths or more than one matching path

 log_utils.py/              # logging and reporting
  [x] setup_logging         # create and customize logging

 text_utils.py/             # human text normalization
  [x] remove_diacritics     # removes diacritics
  [x] canon                 # lower-cases all letters and replaces \s with hyphen
  [x] normalize_phone       # normalizes phone numbers FOR MATCHING: DOES NOT check for valid phone format
  [x] normalize_phone       # normalizes emails FOR MATCHING: DOES NOT check for valid email format
  [ ] is_valid_phone        # check for valid us phone format
  [ ] is_valid_email        # check for valid email format


## 🚧 Next Steps

---

_This document serves as the 30-second mental map of the repo. Update it as functions are created or refactored._
