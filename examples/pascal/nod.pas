var x,y,r: integer;

procedure nod(a,b: integer; var result: integer);
begin
  while a <> b do
  begin
    if a > b then a := a - b else b := b - a;
  end;
  result := a;
end;

procedure nod_mod(a,b: integer; var result: integer);
begin
  while a*b <> 0 do
  begin
    if a > b then a := a mod b else b := b mod a;
  end;
  result := a+b;
end;

begin

  x := 49; y := 21;
  
  nod(x, y, r);
  writeln('НОД(', x, ', ', y, ') = ', r);

  nod_mod(x, y, r);
  writeln('НОД(', x, ', ', y, ') = ', r);

end.
