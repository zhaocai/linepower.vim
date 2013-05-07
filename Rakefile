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
    to File.join(powerline_config_path,f)
  end

end
