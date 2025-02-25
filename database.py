# import aiosqlite3
import asyncio 
import asyncpg


async def connect():
#     conn = await aiosqlite3.connect("./database.db")
#     c = await conn.cursor()
    conn = await asyncpg.connect(dsn = "postgres://zkhimypylyksjl:c8814bf833b7fafa0c76a0f39d9145926e783ff24f78f94d5031344084846ab1@ec2-35-168-65-132.compute-1.amazonaws.com:5432/d3m54ukaiiqmf4")
    
    # conn = await asyncpg.create_pool(dsn = "postgres://postgres:ZPWgpMN4hETqjXAV@207.244.244.19:4082/pterodactyl")
    print("Connection successful")

    await conn.execute("""CREATE TABLE server_details(
            guild_id bigint,
            prefix text,
            modroles text,
            adminroles text,
            cooldown float8
            )""")

    await conn.execute("""CREATE TABLE trigger_response(
            guild_id bigint,
            trigger text,
            response text,
            type text,
            user_id bigint,
            added_time float8
            )""")
    
    await conn.execute("""CREATE TABLE bump_lb(
            guild_id bigint,
            user_id bigint,
            user_count bigint
            )""")

    await conn.close()
    print("Done")

#     await c.execute("""CREATE TABLE to_do(
#             guild_id int,
#             to_do_id int,
#             details text,
#             status text,
#             added_time real
#             )""")
#     await conn.commit()

asyncio.run(connect())
    
