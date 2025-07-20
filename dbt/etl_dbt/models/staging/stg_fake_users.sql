-- models/staging/stg_fake_users.sql

with source as (
    select * from raw.fake_users
)

select
    id,
    lower(name) as name,
    lower(email) as email,
    initcap(city) as city
from source
