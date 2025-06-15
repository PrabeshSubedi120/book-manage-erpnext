# 📚 ERPNext Book Management System

This is a custom ERPNext application built as part of an internship assessment. It allows managing books and their submissions, along with a server-side utility to detect overdue users.

---

## 🚀 Features

- 📘 Book Doctype: Title, Author, Submission Deadline, Status
- ✅ Book Submission Doctype: Linked to Book and User
- 🔍 Server-side script to list overdue users
- 📦 Custom ERPNext app using Frappe Framework

---

## 🛠️ How It Works

- Built using ERPNext v14+ and Frappe Framework
- Uses Custom App `book_manage`
- Server script callable via custom button in Book form:
    - **"Check Overdue Users"** button checks who missed their submission deadline

---

## 📂 Doctypes Created

### `Book`
- Title (Data)
- Author (Data)
- Submission Deadline (Date)
- Status (Select: Available/Issued/Overdue)

### `Book Submission`
- User (Link to User)
- Book (Link to Book)
- Submission Date (Date)
- Status (Select: Submitted/Not Submitted)

---

## ⚙️ Setup Instructions

```bash
# Clone repository
git clone https://github.com/PrabeshSubedi120/book-manage-erpnext.git

# Change directory
cd Book_Management_system

# Install app
bench --site [yoursite] install-app book_manage
