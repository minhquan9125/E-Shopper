# CSS Modular Structure Documentation

## Overview
The main CSS has been separated into modular, organized files for better maintainability and scalability. Each file focuses on specific components or pages.

---

## CSS File Organization

### 1. **index.css** (Main Import File)
- Central file that imports all modular CSS files
- **Usage**: Replace the original `main.css` reference with `index.css` in your HTML files
- Example: `<link rel="stylesheet" href="css/index.css">`

### 2. **typography.css**
- Global typography settings
- Font imports from Google Fonts
- Base element styles (body, h1-h6, links, buttons)
- Scroll-up button animation
- **Contains**: Global animations, typography rules

### 3. **header.css**
- Header styling
- Navigation menu styles
- Search box styling
- Dropdown menu (sub-menu)
- Social icons styling
- **Contains**: All header-related CSS for the top section

### 4. **footer.css**
- Footer layout and styling
- Footer widget sections
- Company info section
- Video gallery styling
- Address section
- Search form in footer
- Social links styling
- **Contains**: Complete footer styling

### 5. **main-home.css**
- Homepage/Main page styling
- Slider and carousel styles
- Category products
- Product showcase layout
- Recommended items carousel
- Partners section
- **Contains**: All homepage specific styles

### 6. **login.css**
- Login form styling
- Login input fields
- Login button styling
- Remember me checkbox
- Social login "OR" divider
- **Contains**: Dedicated login page styles

### 7. **account.css**
- Signup/Registration form styling
- Account creation fields
- Account form inputs and buttons
- Select dropdowns and textarea styling
- **Contains**: Account/signup page specific styles

### 8. **shop.css**
- Shop/Products listing page styles
- Pagination styling
- Product grid layout styles
- **Contains**: Shop page specific styles

### 9. **product-details.css**
- Product detail page styling
- Product image gallery
- Product information section
- Price and quantity picker
- Product reviews section
- Similar products carousel
- **Contains**: Product detail page specific styles

### 10. **cart.css**
- Shopping cart page styles
- Cart table styling
- Cart item management (quantity, delete)
- Cart totals and summary
- Breadcrumbs styling
- User information section
- **Contains**: Complete cart page styling

### 11. **checkout.css**
- Checkout process styling
- Checkout steps/options
- Shipping and billing forms
- Order summary
- Payment options styling
- **Contains**: Checkout page specific styles

### 12. **blog.css**
- Blog listing page styles
- Blog post cards and metadata
- Blog single post/detail page styles
- Blog comments section
- Rating area styles
- Reply/comment box styling
- **Contains**: All blog-related page styles

### 13. **contact.css**
- Contact page styling
- Contact form elements
- Contact information section
- Map container styling
- Social networks section
- **Contains**: Contact page specific styles

### 14. **404.css**
- 404 Error page styling
- Error message styling
- Back to home button
- **Contains**: Error page specific styles

### 15. **utils.css**
- Utility classes
- Rating/stars display
- Text decorations (strikethrough)
- Helper classes
- **Contains**: General utility and helper classes

---

## How to Update Your HTML Files

### Old Method (One Large File)
```html
<link rel="stylesheet" href="css/main.css">
```

### New Method (Modular Files)
```html
<link rel="stylesheet" href="css/index.css">
```

**That's it!** The `index.css` will automatically import all the modular CSS files.

---

## Benefits of This Structure

✅ **Better Organization**: Each CSS file is focused on specific functionality
✅ **Easier Maintenance**: Find and update styles faster
✅ **Scalability**: Easy to add new modules or pages
✅ **Reusability**: Modular components can be shared across pages
✅ **Performance**: Can serve individual files or minify as needed
✅ **Version Control**: Easier to track changes in specific pages
✅ **Team Collaboration**: Multiple team members can work on different CSS modules

---

## File Structure Diagram

```
css/
├── index.css (Main import file)
├── typography.css
├── header.css
├── footer.css
├── main-home.css
├── login.css
├── account.css
├── shop.css
├── product-details.css
├── cart.css
├── checkout.css
├── blog.css
├── contact.css
├── 404.css
├── utils.css
└── [original main.css - can be archived/deleted]
```

---

## Usage Examples

### For Homepage
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="css/index.css"> <!-- Contains all modular styles -->
</head>
<body>
    <!-- Your homepage content -->
</body>
</html>
```

### Why This Works
- `index.css` imports `typography.css`, `header.css`, `footer.css`, and `main-home.css`
- All necessary styles for the homepage are automatically included

---

## Customization

To customize styles for a specific page:
1. Open the corresponding CSS file (e.g., `login.css` for login page)
2. Modify the styles as needed
3. Save the file
4. Changes are immediately reflected (no need to update other files)

---

## Next Steps

1. ✅ Update all HTML files to link `css/index.css` instead of `css/main.css`
2. ✅ Test all pages to ensure styling works correctly
3. ✅ Archive or delete the original `main.css` file
4. ✅ Keep the original as backup if needed

---

## Color Reference

**Primary Color**: `#FE980F` (Orange)
**Dark Gray**: `#363432`
**Light Gray**: `#F0F0E9`
**Text Color**: `#696763`
**Accent**: `#FDB45E` (Light Orange)

These colors are used consistently across all CSS modules.
