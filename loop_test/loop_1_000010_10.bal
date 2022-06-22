import ballerina/io;

public function main() {
    decimal[] values = [11091066072672.14185880932627453096E1536, 85067464177.63873852117030968586833, 132833480.5121317758868596237344416, -2985726845853045282330534081.554635, -6902121175669999647928165188377583E2867, 9311827178676672974903.879282037228, -664788529.7526249200340126905349846, 88279252523505.17213065084770750913E347, 688437780361.5940490150034469929251E5494, -715444.2086189099203425194115480952];
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -37831448348818661978591676949.42735E4195d {
        return 0;
    }
    else if val > -93306062682167727761871.80044027936d {
        return 1;
    }
    else if val > -89663687366856.85770611426743707714d {
        return 2;
    }
    else if val > -160917553280815973143250823668.0714E-2887d {
        return 3;
    }
    else if val > -5020.254198302432843903902292584349E-4897d {
        return 4;
    }
    else if val > 671565457273472546971258900.7931736E-3532d {
        return 5;
    }
    else if val > 2925109720065.957022857914796662776d {
        return 6;
    }
    else if val > 2826921174272835089.636993930184007d {
        return 7;
    }
    else if val > 375423352349.1062618455009199485395E1679d {
        return 8;
    }
    else if val > 56955261668990.42773481857796424124E4636d {
        return 9;
    }
    return 10;
}
