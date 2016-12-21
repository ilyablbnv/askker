var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
    gulp.src('src/assets/sass/**/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('src/static/css/'));
});

//Watch task
gulp.task('watch',function() {
    gulp.watch('src/assets/sass/**/*.sass', ['styles']);
});