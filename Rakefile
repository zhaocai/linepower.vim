require 'rake/distribute'

powerline_src = File.expand_path('~/.vim/bundle/powerline')

desc "diff from system default config"
task :diff_default => [] do
  sh "vimdo dirdiff #{powerline_src}/powerline/config_files config"
end


config_files = FileList["config/**/*.json"]
powerline_config_path = File.expand_path('~/.config/powerline')

config_files.each do |f|
  distribute :FileItem do
    from f
    to   "#{f.pathmap("%{^config,#{powerline_config_path}}p")}"
    diff { |dest, src|
      system %Q{vimdo diff "#{dest}" "#{src}"}
    }
  end
end


desc "show config files"
task :config_files do
  puts config_files
end
