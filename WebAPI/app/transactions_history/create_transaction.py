from scripts.database import get_connection


def create_transaction(connection, item_id, qty, init_qty, end_qty, user, reason):
    transaction_type = "Restock"

    if qty < 0:
        transaction_type = "Withdraw"

    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO transactions (
                item_id,
                item_quantity_changed,
                item_stock_before_transaction,
                item_stock_after_transaction,
                transaction_type,
                by_user,
                reason
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                item_id,
                qty,
                init_qty,
                end_qty,
                transaction_type,
                user,
                reason
            )
        )
        transaction_id = cursor.fetchone()[0]
        return {
            "Transaction ID": transaction_id
        }