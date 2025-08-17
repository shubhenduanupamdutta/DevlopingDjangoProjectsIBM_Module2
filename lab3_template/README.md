# Rendering Dynamic Webpages

Using template and views

---

## Initialize uv independent project

```bash
uv init --no-workspace -p 3.8.13
uv add -r requirements.txt
```

## Some model commands

| **Package/Method**   | **Description**                        | **Code Example**                                     |
| -------------------- | -------------------------------------- | ---------------------------------------------------- |
| `count()`            | Counts the number of objects.          | `MyModel.objects.count()`                            |
| `Sum()`              | Provides the sum of a field.           | `MyModel.objects.aggregate(Sum('field'))`            |
| `Avg()`              | Calculates the average of a field.     | `MyModel.objects.aggregate(Avg('field'))`            |
| `Max()`              | Provides the maximum value of a field. | `MyModel.objects.aggregate(Max('field'))`            |
| `Min()`              | Provides the minimum value of a field. | `MyModel.objects.aggregate(Min('field'))`            |
| `order_by()`         | Orders objects based on a field.       | `MyModel.objects.order_by('field')`                  |
| `order_by('-')`      | Orders objects in descending order.    | `MyModel.objects.order_by('-field')`                 |
| `select_related`     | Performs inner join.                   | `MyModel.objects.select_related('related_model')`    |
| `prefetch_related`   | Performs left outer join.              | `MyModel.objects.prefetch_related('related_model')`  |
| `many_to_many`       | Performs many-to-many join.            | `obj.many_to_many_field.all()`                       |
| `filter(ForeignKey)` | Performs conditional joins.            | `MyModel.objects.filter(related_model__isnull=True)` |
