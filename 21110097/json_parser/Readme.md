# JSON Parser - Enhanced Version

This project extends the functionality of the original JSON parser by introducing additional features while maintaining the core parsing capabilities. The previous implementation remains intact, but new enhancements have been added to improve flexibility and usability.

## **New Features**

### **1. Support for Comments (C++ Style)**
- Single-line comments using `//`
- Comments are ignored during parsing.

### **2. Support for New Literals**
- Recognizes `true`, `false`, and `null` as valid JSON literals.

### **3. Underscore (`_`) Between Numbers**
- Numbers can include a single underscore for readability, e.g., `1_0` (interpreted as `10`).
- Restrictions:
  - Only one underscore is allowed between two digits.
  - Cannot begin or end with an underscore.
  - Invalid cases: `_10`, `10_`, `1__0`.

### **4. Allowing Trailing Commas in Arrays and Objects**
- Arrays can end with a trailing comma, e.g., `[10, 2,]` (valid).
- Objects can also end with a trailing comma, e.g., `{"a": 1, "b": 2,}` (valid).
- Restrictions:
  - Empty arrays with a comma (`[,]`) are **not** allowed.
  - Arrays with multiple consecutive commas (`[10,,]`) are **not** allowed.
  - Similar restrictions apply to objects.

These new features enhance JSON parsing flexibility while ensuring compliance with structured formatting rules.

