import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

try:
    with sqlite3.connect("db/lesson.db") as conn:
        cursor = conn.cursor()

    sql_query = """
    SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
    """

    employee_results = pd.read_sql(sql_query, conn)

    employee_results.plot(
        x="last_name",
        y="revenue",
        kind="bar",
        color="skyblue",
        legend=False
    )
    plt.hist(employee_results)
    plt.title("Employee Salary Information")
    plt.xlabel("Employee last name")
    plt.ylabel("Total revenue")
    plt.show()

except sqlite3.Error as e:
    print(f"Error connecting to SQLite DB: {e}")
