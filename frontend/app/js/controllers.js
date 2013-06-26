'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
    controller('MyCtrl1', [
        '$scope', '$http',
        function ($scope, $http) {
            $scope.files = {
                irma: [
                    'T01_1891.jpg',
                    'T01_1892.jpg',
                    'T01_1893.jpg',
                    'T01_1998.jpg',
                    'T01_2041.jpg',
                    'T01_2042.jpg',
                    'T01_2044.jpg',
                    'T01_2045.jpg',
                    'T01_2046.jpg',
                    'T01_2133.jpg',
                    'T01_2525.jpg',
                    'T01_2526.jpg',
                    'T01_2530.jpg',
                    'T01_2531.jpg',
                    'T01_2532.jpg',
                    'T01_2535.jpg',
                    'T01_2536.jpg',
                    'T01_2538.jpg',
                    'T01_2539.jpg',
                    'T01_2544.jpg',
                    'T02_2143.jpg',
                    'T02_2147.jpg',
                    'T02_2159.jpg',
                    'T02_2161.jpg',
                    'T02_2162.jpg',
                    'T02_2164.jpg',
                    'T02_2166.jpg',
                    'T02_2167.jpg',
                    'T02_2168.jpg',
                    'T02_2170.jpg',
                    'T03_2971.jpg',
                    'T03_2972.jpg',
                    'T03_2975.jpg',
                    'T03_2984.jpg',
                    'T03_2986.jpg',
                    'T03_2989.jpg',
                    'T03_2993.jpg',
                    'T03_2998.jpg',
                    'T03_3016.jpg',
                    'T03_3017.jpg',
                    'T03_3020.jpg',
                    'T03_3023.jpg',
                    'T03_3024.jpg',
                    'T03_3028.jpg',
                    'T03_3032.jpg',
                    'T03_3034.jpg',
                    'T03_3036.jpg',
                    'T03_3044.jpg',
                    'T03_3048.jpg',
                    'T03_3049.jpg',
                    'T04_372290.jpg',
                    'T04_372291.jpg',
                    'T04_372293.jpg',
                    'T04_372294.jpg',
                    'T04_372295.jpg',
                    'T04_372296.jpg',
                    'T04_372297.jpg',
                    'T04_372298.jpg',
                    'T04_372299.jpg',
                    'T04_372302.jpg',
                    'T04_372304.jpg',
                    'T04_372305.jpg',
                    'T04_372306.jpg',
                    'T04_372307.jpg',
                    'T04_372308.jpg',
                    'T04_372309.jpg',
                    'T04_372310.jpg',
                    'T04_372312.jpg',
                    'T04_372313.jpg',
                    'T04_372314.jpg',
                    'T05_3146.jpg',
                    'T05_3147.jpg',
                    'T05_3151.jpg',
                    'T05_3158.jpg',
                    'T05_3161.jpg',
                    'T05_3166.jpg',
                    'T05_3167.jpg',
                    'T05_3170.jpg',
                    'T05_3171.jpg',
                    'T05_3173.jpg',
                    'T05_3179.jpg',
                    'T05_3183.jpg',
                    'T05_3184.jpg',
                    'T05_3186.jpg',
                    'T05_3187.jpg',
                    'T05_3195.jpg',
                    'T05_3196.jpg',
                    'T05_3197.jpg',
                    'T05_3203.jpg',
                    'T05_3210.jpg',
                    'T05_3212.jpg',
                    'T05_3214.jpg',
                    'T05_3220.jpg',
                    'T05_3221.jpg',
                    'T05_3223.jpg',
                    'T05_3225.jpg',
                    'T05_3237.jpg',
                    'T05_3244.jpg',
                    'T05_3253.jpg',
                    'T05_3254.jpg'
                ],
                tramas: [
                    'T01_10.jpg',
                    'T01_20.jpg',
                    'T01_30.jpg',
                    'T01_40.jpg',
                    'T02_10.jpg',
                    'T02_20.jpg',
                    'T02_30.jpg',
                    'T02_40.jpg',
                    'T03_10.jpg',
                    'T03_20.jpg',
                    'T03_30.jpg',
                    'T03_40.jpg',
                    'T04_10.jpg',
                    'T04_20.jpg',
                    'T04_30.jpg',
                    'T04_40.jpg',
                    'T05_10.jpg',
                    'T05_20.jpg',
                    'T05_30.jpg',
                    'T05_40.jpg',
                    'T06_10.jpg',
                    'T06_20.jpg',
                    'T06_30.jpg',
                    'T06_40.jpg',
                    'T07_10.jpg',
                    'T07_20.jpg',
                    'T07_30.jpg',
                    'T07_40.jpg',
                    'T08_10.jpg',
                    'T08_20.jpg',
                    'T08_30.jpg',
                    'T08_40.jpg',
                    'T09_10.jpg',
                    'T09_20.jpg',
                    'T09_30.jpg',
                    'T09_40.jpg',
                    'T10_10.jpg',
                    'T10_20.jpg',
                    'T10_30.jpg',
                    'T10_40.jpg',
                    'T11_10.jpg',
                    'T11_20.jpg',
                    'T11_30.jpg',
                    'T11_40.jpg',
                    'T12_10.jpg',
                    'T12_20.jpg',
                    'T12_30.jpg',
                    'T12_40.jpg',
                    'T13_10.jpg',
                    'T13_20.jpg',
                    'T13_30.jpg',
                    'T13_40.jpg',
                    'T14_10.jpg',
                    'T14_20.jpg',
                    'T14_30.jpg',
                    'T14_40.jpg',
                    'T15_10.jpg',
                    'T15_20.jpg',
                    'T15_30.jpg',
                    'T15_40.jpg',
                    'T16_10.jpg',
                    'T16_20.jpg',
                    'T16_30.jpg',
                    'T16_40.jpg',
                    'T17_10.jpg',
                    'T17_20.jpg',
                    'T17_30.jpg',
                    'T17_40.jpg',
                    'T18_10.jpg',
                    'T18_20.jpg',
                    'T18_30.jpg',
                    'T18_40.jpg',
                    'T19_10.jpg',
                    'T19_20.jpg',
                    'T19_30.jpg',
                    'T19_40.jpg',
                    'T20_10.jpg',
                    'T20_20.jpg',
                    'T20_30.jpg',
                    'T20_40.jpg',
                    'T21_10.jpg',
                    'T21_20.jpg',
                    'T21_30.jpg',
                    'T21_40.jpg',
                    'T22_10.jpg',
                    'T22_20.jpg',
                    'T22_30.jpg',
                    'T22_40.jpg',
                    'T23_10.jpg',
                    'T23_20.jpg',
                    'T23_30.jpg',
                    'T23_40.jpg',
                    'T24_10.jpg',
                    'T24_20.jpg',
                    'T24_30.jpg',
                    'T24_40.jpg',
                    'T25_10.jpg',
                    'T25_20.jpg',
                    'T25_30.jpg',
                    'T25_40.jpg'
                ]
            };

            $scope.currentDataset = 'irma';
            $scope.currentMethod = 'glcm';
            $scope.currentFilename = undefined;

            $scope.results = [];

            $scope.currentPreview = '';

            $scope.setCurrentPreview = function (filename) {
                $scope.currentPreview = filename;
            };

            /* MAIN PROCESSING - KOHONEN */
            $scope.classes = {
                irma: 5,
                tramas: 25
            };

            // getting data from file
            $scope.run = function (filename) {
                var url = 'data/' + $scope.currentDataset +
                    '_' + $scope.currentMethod + '.json';
                $http.get(url).success(function (data) {
                    $scope.points = data;

                    //maxes vector for generating centers within the points zone
                    var maxes = [];
                    for (var i = 0; i < $scope.points[Object.keys($scope.points)[0]].length; i++) {
                        maxes.push(0);
                    }

                    //calculating maxes for each feature
                    for (var i in $scope.points) {
                        for (var j = 0; j < $scope.points[Object.keys($scope.points)[0]].length; j++) {
                            if ($scope.points[i][j] > maxes[j])
                                maxes[j] = $scope.points[i][j];
                        }
                    }

                    // initializing initial centers
                    var centers = [], prev_centers = [], elements = [];
                    for (var i = 0; i < $scope.classes[$scope.currentDataset]; i++) {
                        centers.push([]);
                        for (var j = 0; j < $scope.points[Object.keys($scope.points)[0]].length; j++) {
                            centers[i].push(Math.random() * maxes[j]);
                        }
                    }
                    for (var i = 0; i < centers.length; i++) {
                        prev_centers.push([]);
                        prev_centers[i] = centers[i].slice();
                    }

                    for (var i in $scope.points) {
                        elements.push($scope.points[i]);
                    }

                    // kohonen variables
                    var n = 0.6,
                    n_rate=0.5,
                    eps=0.0001,
                    difference = eps + 1;

                    // euclidian distance
                    var distance = function (a, b) {
                        var dist = 0;
                        for (var i = 0; i < a.length; i++) {
                            dist += Math.pow(a[i]-b[i], 2);
                        }
                        return dist;
                    }

                    // main kohonen classification
                    while (difference > eps) {
                        difference = 0;
                        // for each element
                        for (var i = 0; i < elements.length; i++) {
                            // getting min distance in order to get J
                            var min = 0, min_dist = distance(elements[i], centers[0]);
                            for (var j = 1; j < centers.length; j++) {
                                if (distance(elements[i], centers[j]) < min_dist) {
                                    min = j;
                                    min_dist = distance(elements[i], centers[j]);
                                }
                            }

                            // updating J
                            for (var j = 0; j < centers[min].length; j++) {
                                centers[min][j] = centers[min][j] +
                                    n*(elements[i][j] - centers[min][j]);
                            }

                        }

                        for (var i = 0; i < centers.length; i++) {
                            for (var j = 0; j < centers[i].length; j++) {
                                difference += Math.abs(centers[i][j] - prev_centers[i][j]);
                            }
                        }
                        console.log(difference);
                        n = n * n_rate;

                        for (var i = 0; i < centers.length; i++) {
                            prev_centers[i] = centers[i].slice();
                        }

                    }

                    // getting results
                    var min = 0, min_dist = distance($scope.points[filename], centers[0]);
                    for (var i = 1; i < centers.length; i++) {
                        if (distance($scope.points[filename], centers[i]) < min_dist) {
                            min = i;
                            min_dist = distance($scope.points[filename], centers[i]);
                        }
                    }

                    // getting distances from chosen cluster
                    var buff = new Array(100), count = 0;
                    for (var i in $scope.points) {
                        buff[count] = {
                            filename: i,
                            features: $scope.points[i],
                            distance:distance($scope.points[i], centers[min])
                        };
                        count++;
                    }

                    function compare_dist (a, b) {
                        if (a.distance < b.distance) {
                            return -1
                        }
                        if (a.distance === b.distance) {
                            return 0;
                        }
                        else return 1;
                    }

                    buff.sort(compare_dist);
                    $scope.results = buff.slice(0, 10);
                });

            };

            $scope.$watch('currentFilename', function () {
                if ($scope.files[$scope.currentDataset].indexOf($scope.currentFilename) !== -1) {
                    $scope.run($scope.currentFilename);
                }
            });

            $scope.$watch('currentMethod', function () {
                $scope.run($scope.currentFilename);
            });
        }]);
