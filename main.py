#arith_server.py
from fastmcp import FastMCP
from __future__ import annotations
mcp=FastMCP("arith")

def _as_number(x):
    #accept ints/floats or numeric strings; raise clean errors otherwise
    if isinstance(x(int,float)):
        return float(x)
    if isinstance(x(str)):
        return float(x.strip())
    raise TypeError("except a number (int/float or numeric string)")

@mcp.tool()
async def add(a:float ,b:float)->float:
    """Return a+b."""
    return _as_number(a)+_as_number(b)

@mcp.tool()
async def subtract(a:float ,b:float)->float:
    """Return a-b."""
    return _as_number(a)-_as_number(b)

@mcp.tool()
async def multiply(a:float ,b:float)->float:
    """Return a*b."""
    return _as_number(a)*_as_number(b)

@mcp.tool()
async def divide(a:float ,b:float)->float:
    """Return a/b."""
    return _as_number(a)/_as_number(b)

@mcp.tool()
async def power(a:float ,b:float)->float:
    """Return a**b."""
    return _as_number(a)**_as_number(b)

@mcp.tool()
async def modulus(a:float ,b:float)->float:
    """Return a%b.Raise on modulus zero"""
    a=_as_number(a)
    b=_as_number(b)
    if b==0:
        raise ZeroDivisionError("modulus by zero")
    return a%b

def main():
    mcp.run()


if __name__ == "__main__":
    main()