import ballerina/io;

public function main() {
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -785787104984906.3542667409921844144d {
        return 0;
    }
    else if val > -4553261527.941439783116746027017533d {
        return 1;
    }
    else if val > -8.227578714589697751019204398552142d {
        return 2;
    }
    else if val > -4184887821.949302607468714838873152E-4695d {
        return 3;
    }
    else if val > -76188787315849.45269370335349182660E-5291d {
        return 4;
    }
    else if val > -5535367415606279218.156353911185083E-5539d {
        return 5;
    }
    else if val > 253873461321526269131492.0719391949E-5058d {
        return 6;
    }
    else if val > 77.65288380408821282580347630967122E-3152d {
        return 7;
    }
    else if val > 72919.1605015706893216325603901649d {
        return 8;
    }
    else if val > 810987511729868946393093345868.9105d {
        return 9;
    }
    return 10;
}