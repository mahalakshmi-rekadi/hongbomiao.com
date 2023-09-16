import config
import pandas as pd
from sqlalchemy import create_engine, text
from trino.sqlalchemy import URL


def remove_dataframe_duplicate_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()
    df = df.loc[:, ~df.columns.duplicated()]
    return df


def main():
    engine = create_engine(
        URL(host=config.trino_host, port=config.trino_port, user=config.trino_user)
    )
    with engine.connect() as conn:
        cols = ", ".join(["current", "voltage", "temperature"])
        params = {"event_id": "ad7953cd-6d49-4929-8180-99555bebc255"}
        sql_query = text(
            f"""
            with
            t0 as (select * from delta.hm_delta_db.motor_data_0 where _event_id = :event_id),
            t1 as (select * from delta.hm_delta_db.motor_data_1 where _event_id = :event_id),
            t2 as (select * from delta.hm_delta_db.motor_data_2 where _event_id = :event_id),
            t3 as (select * from delta.hm_delta_db.motor_data_3 where _event_id = :event_id),
            t4 as (select * from delta.hm_delta_db.motor_data_4 where _event_id = :event_id),
            t5 as (select * from delta.hm_delta_db.motor_data_5 where _event_id = :event_id),
            t6 as (select * from delta.hm_delta_db.motor_data_6 where _event_id = :event_id),
            t7 as (select * from delta.hm_delta_db.motor_data_7 where _event_id = :event_id),
            t8 as (select * from delta.hm_delta_db.motor_data_8 where _event_id = :event_id),
            t9 as (select * from delta.hm_delta_db.motor_data_9 where _event_id = :event_id),
            ta as (select * from delta.hm_delta_db.motor_data_a where _event_id = :event_id),
            tb as (select * from delta.hm_delta_db.motor_data_b where _event_id = :event_id),
            tc as (select * from delta.hm_delta_db.motor_data_c where _event_id = :event_id),
            td as (select * from delta.hm_delta_db.motor_data_d where _event_id = :event_id),
            te as (select * from delta.hm_delta_db.motor_data_e where _event_id = :event_id),
            tf as (select * from delta.hm_delta_db.motor_data_f where _event_id = :event_id)
            select from_unixtime(t0._time / 1000.0) AS _time, {cols}
            from t0
            join t1 on t0._time = t1._time
            join t2 on t0._time = t2._time
            join t3 on t0._time = t3._time
            join t4 on t0._time = t4._time
            join t5 on t0._time = t5._time
            join t6 on t0._time = t6._time
            join t7 on t0._time = t7._time
            join t8 on t0._time = t8._time
            join t9 on t0._time = t9._time
            join ta on t0._time = ta._time
            join tb on t0._time = tb._time
            join tc on t0._time = tc._time
            join td on t0._time = td._time
            join te on t0._time = te._time
            join tf on t0._time = tf._time
            order by t0._time asc
            """
        )
        res = conn.execute(sql_query, params)
        df = pd.DataFrame(res.fetchall(), columns=res.keys())
        print(df)


if __name__ == "__main__":
    main()
