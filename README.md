# Django Project for learning Django (Twitter Clone)

## Difference b/w null=True & blank=True for model fields

If you only set blank=True, the form will allow empty input, but the database will still expect a non-NULL value unless you provide a default. Similarly, if you set only null=True, the form will still require an input for the field.

So, using both ensures that:

The field is optional in forms.
The field can store NULL in the database if left empty.
